# 02｜Instagram Lead Discovery

本任务先把“搜索账号”升级为一个可验收的业务对象：发现并筛选潜在 wig salon 类商业账号，形成可人工复核的 Lead List。

## Plan First

执行前先确认：国家 / 城市、目标是 salon、stylist、wig store 或全部、用途是市场观察还是潜客开发、目标数量，以及必须排除的账号。不要自行替业务方决定。

## 执行模式

- Live Mode：仅使用公开可见网页或搜索结果。
- Offline Fallback：Live 受阻时，使用 `input/offline/search-results.html` 与 `input/offline/profiles/` 中 18 个虚构教学 Profile。

候选可分为：Salon、Independent Stylist、Wig Store、Beauty Supply、Brand / E-commerce、Consumer / Irrelevant、Uncertain。

## 建议字段

`Account`、`Display Name`、`Profile URL`、`Location`、`Category`、`Bio Summary`、`Website / Public Contact`、`Follower Count`、`Activity Signal`、`Why Matched`、`Why Rejected / Risk`、`Source`、`Confidence`、`Manual Review`。

位置、粉丝数和联系方式只有公开可见时才记录；简介没有写城市时不得从照片、区号或风格自行判断。

## 边界

只处理公开信息；不访问私人内容，不自动关注，不自动私信，不做批量营销，不推测私人联系方式。搜不到不等于不存在，名单必须保留 source URL。

## 输出契约

只在 `outputs/` 创建：

- `lead-list.xlsx`
- `discovery-notes.md`

Notes 应记录搜索范围、时间、筛选规则、排除规则、来源限制、缺失字段与人工复核项。原始输入不得覆盖。

