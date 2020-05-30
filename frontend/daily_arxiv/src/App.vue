<template>
  <div id="app">
    <ArxivPapers msg="Arxiv Papers"/>
    
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import ArxivPapers from './components/ArxivPapers.vue'

export default {
  name: 'App',
  components: {
    ArxivPapers
  }
}
</script>

<style>
body{
  margin:0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0px;
  padding: 0px;
}
</style>
