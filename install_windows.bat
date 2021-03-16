cd %systemdrive%%homepath%
del /Q /S /F %systemdrive%%homepath%\\hentcli
mkdir hentcli
cd hentcli
setx PYTHONPATH "%PYTHONPATH%%systemdrive%%homepath%\\hentcli"
setx PATH "%PATH%%systemdrive%%homepath%\\hentcli"
py -m pip install timg rule34
mkdir images
curl.exe --output python_hentai.py --url http://xn--jha.xyz/hentcli/python_hentai.py
curl.exe --output r34.py --url http://xn--jha.xyz/hentcli/r34.py
curl.exe --output hentcli.bat --url http://xn--jha.xyz/hentcli/hentcli.bat