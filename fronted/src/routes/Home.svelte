<script>
    let question_list = []

    function get_question_list() {
        fetch("https://ya2301.ebesesk.synology.me/api/question/list").then((response) => {
            response.json().then((json) => {
                question_list = json
            })
        })
    }

    get_question_list()
</script>

<ul>
    {#each question_list as question}
        <li>{question.subject}</li>
    {/each}
</ul>