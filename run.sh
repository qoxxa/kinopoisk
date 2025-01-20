#run.sh
results=./results
rep_history=./final-report/history
report=./final-report

rm -rf $results # Удалить папку с результатами
pytest --allure=$results # Запустить тесты
mv $rep_history $results # Перенести историю в результаты
rm -rf $report # Удалить отчет
allure generate $results -o $report # Сгенерировать отчет
allure open $report # Открыть отчет