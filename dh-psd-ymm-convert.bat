@rem 文字コード Shift-JIS -> UTF-8 変更
chcp 65001

@rem 参照するファイルを更新
copy "./00-full-psd" "./dist/dh-psd-ymm-convert/00-full-psd"
copy "./00-icon-psd" "./dist/dh-psd-ymm-convert/00-icon-psd"

@rem Touhou-LW-Farm-Quest-RPA.exe 起動
cd ./dist/dh-psd-ymm-convert
dh-psd-ymm-convert.exe

@rem 参照するファイルを更新
@rem copy "./00-result" "../../00-result"
cd ../..
xcopy /e "./dist/dh-psd-ymm-convert/00-result" "./00-result"

echo 終了するには何かキーを押してください...
pause > nul
exit