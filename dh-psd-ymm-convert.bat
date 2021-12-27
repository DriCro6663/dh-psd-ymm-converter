@rem 文字コード Shift-JIS -> UTF-8 変更
chcp 65001

@rem 参照するファイルを更新
cd ./dist/dh-psd-ymm-convert
rmdir "./00-def-psd"
rmdir "./00-sta-psd"
rmdir "./01-result"
mkdir "./00-def-psd"
mkdir "./00-sta-psd"
mkdir "./01-result"
cd ../..
copy "./00-def-psd" "./dist/dh-psd-ymm-convert/00-def-psd"
copy "./00-sta-psd" "./dist/dh-psd-ymm-convert/00-sta-psd"

@rem Touhou-LW-Farm-Quest-RPA.exe 起動
cd ./dist/dh-psd-ymm-convert
dh-psd-ymm-convert.exe

@rem 参照するファイルを更新
cd ../..
xcopy /e "./dist/dh-psd-ymm-convert/01-result" "./01-result"

echo 終了するには何かキーを押してください...
pause > nul
exit