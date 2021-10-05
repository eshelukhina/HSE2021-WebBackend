# HSE2021-WebBackend

## Запуск проекта

* Командой `uvicorn main:app --reload` в терминале, а затем `open http://localhost:8000`

## Примеры запросов
* `add` позволяет добавить человека в общую "базу данных"
* `info` позволяет посмотреть данные о людях, которые уже добавлены

* ```
  {
      add(firstname:"Katya", lastname:"Shelukhina", age:12){
         lastname
         age
      }
      info(id:1){
         firstname
      }
  }

