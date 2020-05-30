<template>
  <div class="arxiv-papers">
    <div class="title-container">
      <h1 class="title">Daily Arxiv Papers</h1>
    </div>
    <ol>
        <li v-for="p in this.papers" :key="p.id">
            <h2 class="paper-title">{{ p.title.toString().replace("\nTitle :", "") }}</h2>
            <h2 class="paper-id">{{ p.id }}</h2>
            <p> {{p.subjects.toString().replace("\nSubjects: ", "")}}</p>

        </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: 'ArxivPapers',
  props: {
    msg: String
  },
  data () {
      return {
      papers: "Reading..."
      }
  },
  mounted () {
      console.log("Pulling arxiv papers...")
      this.$http
      .get('/papers')
      .then(response => (this.papers = response.data))
      console.log(this.papers)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1.title{
  color: #ffffff;
  font-family: 'Lucida Grande', helvetica, arial, verdana, sans-serif;
  font-size: 2.5em;
  font-weight: normal;
}

div.title-container{
  background-color: #b31c1b;
  padding: 10px 0 10px 0;
  border-bottom: 2px solid #ccc;
}

h2.paper-title{
  color: #212121;
}

h2.paper-id{
  color: #767676;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
