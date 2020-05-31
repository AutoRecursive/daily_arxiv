<template>
  <div class="arxiv-papers">
    <div class="title-container">
      <h1 class="title">Daily Arxiv Papers</h1>
    </div>
    <div class = row>
      <ol>
          <li v-for="p in this.papers" :key="p.id">
            <Card :title="p.title" :id="p.id" :subjects="p.subject_split" :link="p.link" />
            
          </li>
      </ol>
    </div>
  </div>
</template>

<script>
import Card from './Card.vue'

export default {
  name: 'ArxivPapers',
  props: {
    msg: String
  },
  components: {
    Card
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
  font-family: 'Lucida Grande';
  font-size: 2.5em;
  font-weight: normal;
  margin: auto;

}

div.title-container{
  background-color: #b31c1b;
  padding: 10px 0 10px 0;
  border-bottom: 2px solid #ccc;
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
  color: #b31c1b;
}

div.row{
	display:flex;
  align-items: center;
	justify-content:center;
	margin-top:50px;
}
</style>
