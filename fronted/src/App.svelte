<script>
  let message;

  fetch("https://ya2301.ebesesk.synology.me/hello").then((response) => {
    response.json().then((json) => {
      message = json.message;
    });
  });
</script>

<h1>{message}</h1>