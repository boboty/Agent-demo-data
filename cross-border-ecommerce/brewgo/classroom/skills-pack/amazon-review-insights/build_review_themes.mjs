import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const inputPath = "demo/input/reviews.csv";
const outputDir = "outputs";
const outputPath = `${outputDir}/review-themes.xlsx`;

function parseCsv(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (ch === '"') quoted = false;
      else field += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ',') { row.push(field); field = ""; }
    else if (ch === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += ch;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  const headers = rows.shift();
  return rows.filter(r => r.some(v => v !== "")).map(r => Object.fromEntries(headers.map((h, i) => [h, r[i] ?? ""])));
}

const themeByTitle = {
  "Consistent grind": ["优势", "研磨均匀、手冲表现稳定"],
  "Great for travel": ["优势", "便携、无需电池"],
  "Solid hand feel": ["优势", "握持稳、折叠手柄舒适"],
  "Quick routine clean": ["优势", "刷子便于日常快速清理"],
  "Capacity is limited": ["痛点", "多人冲煮时容量偏小"],
  "Adjustment takes practice": ["产品/使用问题", "调节刻度不直观、设定易丢失"],
  "Box arrived damaged": ["包装/物流问题", "运输箱受压破损"],
  "Expected an electric grinder": ["能力误解", "误以为是电动磨豆机"],
  "Grounds in the gap": ["产品/使用问题", "细粉积在调节区缝隙"],
  "Capacity works for me": ["矛盾证据", "30克容量适合两小杯"],
};

const csvText = await fs.readFile(inputPath, "utf8");
const reviews = parseCsv(csvText.replace(/^\uFEFF/, ""));
const workbook = Workbook.create();
const summary = workbook.worksheets.add("Theme Summary");
const evidence = workbook.worksheets.add("Evidence");

const evidenceHeaders = ["review_id", "rating", "title", "review_text", "verified_purchase", "review_date", "variant", "类别", "主题", "标准化文本组", "未来日期标记"];
const evidenceRows = reviews.map(r => {
  const [category, theme] = themeByTitle[r.title];
  return [
    r.review_id, Number(r.rating), r.title, r.review_text, r.verified_purchase,
    new Date(`${r.review_date}T00:00:00Z`), r.variant, category, theme, r.title,
    r.review_date > "2026-08-19" ? "是" : "否",
  ];
});
evidence.getRangeByIndexes(0, 0, 1, evidenceHeaders.length).values = [evidenceHeaders];
evidence.getRangeByIndexes(1, 0, evidenceRows.length, evidenceHeaders.length).values = evidenceRows;
const evidenceTable = evidence.tables.add(`A1:K${evidenceRows.length + 1}`, true, "EvidenceTable");
evidenceTable.style = "TableStyleMedium2";
evidence.freezePanes.freezeRows(1);
evidence.showGridLines = false;
evidence.getRange("A1:K1").format = { fill: "#0F766E", font: { bold: true, color: "#FFFFFF" }, rowHeight: 28, verticalAlignment: "center" };
evidence.getRange(`B2:B${evidenceRows.length + 1}`).format.numberFormat = "0";
evidence.getRange(`F2:F${evidenceRows.length + 1}`).format.numberFormat = "yyyy-mm-dd";
evidence.getRange(`A2:K${evidenceRows.length + 1}`).format.verticalAlignment = "top";
evidence.getRange(`D2:D${evidenceRows.length + 1}`).format.wrapText = true;
const widths = { A: 12, B: 8, C: 25, D: 72, E: 18, F: 14, G: 18, H: 16, I: 32, J: 24, K: 16 };
for (const [col, width] of Object.entries(widths)) evidence.getRange(`${col}:${col}`).format.columnWidth = width;
evidence.getRange(`A2:K${evidenceRows.length + 1}`).format.rowHeight = 38;

summary.showGridLines = false;
summary.mergeCells("A1:N1");
summary.getRange("A1").values = [["BrewGo G2 Amazon 评论主题汇总"]];
summary.getRange("A1:N1").format = { fill: "#134E4A", font: { bold: true, color: "#FFFFFF", size: 16 }, rowHeight: 34, verticalAlignment: "center" };
summary.mergeCells("A2:N2");
summary.getRange("A2").values = [["样本内信号｜分析日 2026-08-19｜频次与严重度分开判断；建议均需进一步验证"]];
summary.getRange("A2:N2").format = { fill: "#CCFBF1", font: { color: "#115E59", italic: true }, rowHeight: 25, verticalAlignment: "center" };

summary.getRange("A4:M4").values = [["样本量", null, "平均评分", null, "已验证购买率", null, "未来日期", null, "唯一文本组", null, "变体数", null, "数据期"]];
summary.getRange("A5:M5").formulas = [[
  "=COUNTA('Evidence'!A2:A61)", null,
  "=AVERAGE('Evidence'!B2:B61)", null,
  "=COUNTIF('Evidence'!E2:E61,\"Y\")/COUNTA('Evidence'!A2:A61)", null,
  "=COUNTIF('Evidence'!K2:K61,\"是\")", null,
  "=10", null,
  "=3", null,
  "=\"2026-05-03 至 2026-08-29\"",
]];
for (const cell of ["A4:B5", "C4:D5", "E4:F5", "G4:H5", "I4:J5", "K4:L5", "M4:N5"]) {
  summary.getRange(cell).format = { fill: cell.includes("4:") ? "#F0FDFA" : "#FFFFFF", borders: { preset: "outside", style: "thin", color: "#99F6E4" } };
}
summary.getRange("A4:M4").format.font = { bold: true, color: "#115E59" };
summary.getRange("A5:M5").format.font = { bold: true, color: "#0F172A", size: 12 };
summary.getRange("C5").format.numberFormat = "0.00";
summary.getRange("E5").format.numberFormat = "0.0%";

summary.getRange("A7:C7").values = [["评分", "评论数", "占比"]];
summary.getRange("A8:A11").values = [[5], [4], [3], [2]];
summary.getRange("B8").formulas = [["=COUNTIF('Evidence'!B2:B61,A8)"]];
summary.getRange("B8:B11").fillDown();
summary.getRange("C8").formulas = [["=B8/$A$5"]];
summary.getRange("C8:C11").fillDown();
summary.getRange("C8:C11").format.numberFormat = "0.0%";
summary.getRange("A7:C11").format.borders = { preset: "outside", style: "thin", color: "#CBD5E1" };
summary.getRange("A7:C7").format = { fill: "#0F766E", font: { bold: true, color: "#FFFFFF" } };

summary.mergeCells("E7:N7");
summary.getRange("E7").values = [["数据质量提示"]];
summary.getRange("E7:N7").format = { fill: "#B45309", font: { bold: true, color: "#FFFFFF" } };
summary.mergeCells("E8:N11");
summary.getRange("E8").values = [["去除统一的“Review sample …”尾句后仅 10 种独立文本；5 条记录日期晚于分析日。主题频次可准确描述这批样本，但不宜外推为真实市场发生率。"]];
summary.getRange("E8:N11").format = { fill: "#FFF7ED", font: { color: "#7C2D12" }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: "#FDBA74" } };

const themeRows = [
  ["优势", "研磨均匀、手冲表现稳定", "", "", "", "强正向", "—", "保持", "三个变体", "R001, R006, R012", "评论直接关联研磨均匀与杯中一致性", "高", "否", "持续监测真实评论中是否稳定出现"],
  ["优势", "便携、无需电池", "", "", "", "强正向", "—", "保持", "三个变体", "R013, R018, R022", "工作包、露营和无电场景", "高", "否", "验证不同出行场景的携带体验"],
  ["优势", "握持稳、折叠手柄舒适", "", "", "", "正向", "—", "保持", "三个变体", "R023, R027, R030", "偏单杯使用场景", "高", "否", "验证连续研磨时舒适度"],
  ["优势", "刷子便于日常快速清理", "", "", "", "正向", "—", "保持", "三个变体", "R031, R034, R036", "对表面浮粉清理有效", "高", "否", "区分表面清理与调节区深度清理"],
  ["痛点", "多人冲煮时容量偏小", "", "", "", "中性/负向", "中", "P1", "三个变体", "R037, R041, R044", "30克低于多人冲煮预期；R060 提供反例", "高", "是", "先验证容量—杯数说明能否降低错配"],
  ["产品/使用问题", "调节刻度不直观、设定易丢失", "", "", "", "强负向", "高", "P0", "三个变体", "R045, R048, R050", "影响核心设定与复现流程", "高", "是", "可用性测试视觉标记、零点和设定记忆"],
  ["包装/物流问题", "运输箱受压破损", "", "", "", "强负向", "中", "P1", "三个变体", "R051, R052, R054", "机身仍工作；根因尚未确认", "中", "是", "检查外箱规格、空隙和仓配节点"],
  ["能力误解", "误以为是电动磨豆机", "", "", "", "强负向", "中", "P1", "三个变体", "R055, R056, R057", "购买前未理解手摇属性", "高", "是", "验证首屏是否清楚表达manual/hand/no battery"],
  ["产品/使用问题", "细粉积在调节区缝隙", "", "", "", "强负向", "中", "P2", "Black, Silver", "R058, R059", "具体但低频的清洁死角", "中", "是", "实物复现后评估结构、刷具或拆洗指引"],
  ["矛盾证据", "30克容量适合两小杯", "", "", "", "强正向", "—", "验证", "Travel Kit", "R060", "与容量偏小主题相反，显示场景差异", "低", "是", "按人数、杯量和冲煮方式分层验证"],
];
const headers = ["类别", "主题", "提及数", "样本占比", "平均评分", "评分信号", "严重度", "建议优先级", "影响变体", "代表评论ID", "证据说明", "置信度", "需人工确认", "验证假设"];
summary.getRange("A13:N13").values = [headers];
summary.getRange(`A14:N${13 + themeRows.length}`).values = themeRows;
for (let row = 14; row <= 13 + themeRows.length; row++) {
  summary.getRange(`C${row}`).formulas = [[`=COUNTIF('Evidence'!I2:I61,B${row})`]];
  summary.getRange(`D${row}`).formulas = [[`=C${row}/$A$5`]];
  summary.getRange(`E${row}`).formulas = [[`=AVERAGEIF('Evidence'!I2:I61,B${row},'Evidence'!B2:B61)`]];
}
summary.getRange(`D14:D${13 + themeRows.length}`).format.numberFormat = "0.0%";
summary.getRange(`E14:E${13 + themeRows.length}`).format.numberFormat = "0.0";
const themeTable = summary.tables.add(`A13:N${13 + themeRows.length}`, true, "ThemeSummaryTable");
themeTable.style = "TableStyleMedium4";
summary.freezePanes.freezeRows(13);
summary.getRange("A13:N13").format = { fill: "#0F766E", font: { bold: true, color: "#FFFFFF" }, rowHeight: 32, verticalAlignment: "center" };
summary.getRange(`A14:N${13 + themeRows.length}`).format = { verticalAlignment: "top", wrapText: true, rowHeight: 54 };
summary.getRange(`H14:H${13 + themeRows.length}`).conditionalFormats.add("containsText", { text: "P0", format: { fill: "#FEE2E2", font: { bold: true, color: "#991B1B" } } });
summary.getRange(`H14:H${13 + themeRows.length}`).conditionalFormats.add("containsText", { text: "P1", format: { fill: "#FFEDD5", font: { bold: true, color: "#9A3412" } } });
summary.getRange(`H14:H${13 + themeRows.length}`).conditionalFormats.add("containsText", { text: "P2", format: { fill: "#FEF9C3", font: { bold: true, color: "#854D0E" } } });
const summaryWidths = [16, 34, 10, 12, 12, 14, 10, 14, 18, 22, 38, 10, 14, 42];
for (let i = 0; i < summaryWidths.length; i++) summary.getRangeByIndexes(0, i, 23, 1).format.columnWidth = summaryWidths[i];

await fs.mkdir(outputDir, { recursive: true });
const checks = await workbook.inspect({ kind: "table", range: "'Theme Summary'!A1:N23", include: "values,formulas", tableMaxRows: 23, tableMaxCols: 14, maxChars: 12000 });
console.log(checks.ndjson);
const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "final formula error scan" });
console.log(errors.ndjson);
for (const sheetName of ["Theme Summary", "Evidence"]) {
  const preview = await workbook.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${outputDir}/${sheetName.replaceAll(" ", "-").toLowerCase()}-preview.png`, new Uint8Array(await preview.arrayBuffer()));
}
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
console.log(`SAVED ${outputPath}`);
