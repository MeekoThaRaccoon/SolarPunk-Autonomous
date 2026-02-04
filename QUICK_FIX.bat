@echo off
echo Creating SolarPunk files...
echo print("Agent ready") > agent.py
echo <html><body><h1>Working</h1></body></html> > dist\index.html
mkdir connected 2>nul
echo ✅ Done. Run: python agent.py
pause