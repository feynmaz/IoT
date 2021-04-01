def fill_ids_file():
    with sqlite3.connect('db.sqlite3') as conn:
        c = conn.cursor()
        for i in range(1000):
            c.execute('insert into guests(guest_id,is_in) values (?,?)',(generate(),False))
        conn.commit()


<script>
        async function runScript() {
            let response = await fetch(url = 'easy_func')
            response.text().then((res) => {
                console.log(res)
            })
        }
    </script>