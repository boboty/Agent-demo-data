@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "SOURCE_DIR=%~dp0skills"
if not defined USERPROFILE (
  echo ERROR: USERPROFILE is not available.
  exit /b 1
)
set "TARGET_DIR=%USERPROFILE%\.agents\skills"
set "SKILLS=amazon-review-insights amazon-return-reduction amazon-inventory-watch amazon-listing-localizer amazon-a-plus-planner supplier-quote-compare customer-service-triage business-file-organizer"

echo BrewGo Codex Skills installer
echo Target: %TARGET_DIR%

for %%S in (%SKILLS%) do (
  if not exist "%SOURCE_DIR%\%%S\SKILL.md" (
    echo ERROR: missing package file: skills\%%S\SKILL.md
    exit /b 1
  )
)

set "HAS_CONFLICT=0"
for %%S in (%SKILLS%) do (
  if exist "%TARGET_DIR%\%%S" (
    echo Existing skill: %%S
    set "HAS_CONFLICT=1"
  )
)

if "%HAS_CONFLICT%"=="1" (
  echo Existing same-name skills will be backed up before installation.
  set /p "ANSWER=Continue? [y/N] "
  if /I not "!ANSWER!"=="Y" if /I not "!ANSWER!"=="YES" (
    echo Installation cancelled; no existing skill was changed.
    exit /b 1
  )
)

for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd-HHmmss"') do set "STAMP=%%I"
if not defined STAMP set "STAMP=backup"
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

for %%S in (%SKILLS%) do (
  if exist "%TARGET_DIR%\%%S" (
    move "%TARGET_DIR%\%%S" "%TARGET_DIR%\%%S.backup-!STAMP!" >nul
    if errorlevel 1 (
      echo ERROR: could not back up %%S. Installation stopped.
      exit /b 1
    )
    echo Backed up: %%S
  )
  xcopy "%SOURCE_DIR%\%%S" "%TARGET_DIR%\%%S\" /E /I /H /Y >nul
  if errorlevel 1 (
    echo ERROR: could not install %%S.
    exit /b 1
  )
)

echo.
echo Installed 8 BrewGo Skills:
for %%S in (%SKILLS%) do echo   - %%S
echo.
echo Codex normally detects new skills automatically. If they do not appear in Skills or /skills, restart Codex.
endlocal
exit /b 0

