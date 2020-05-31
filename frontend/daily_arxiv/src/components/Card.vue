<template>
  <div class="card">
    <div class='card-header'>
      <h3 class="paper-title">{{ title }}</h3>
    </div>
    <div class = 'card-content'>
      <div class='link-container'>
            <a v-bind:href="link" class="paper-id">{{ id }}</a>
      </div>
      <ol>
          <li v-for="subj in subjects" :key="subj.id">
            <p class="card-content-text">{{subj}}</p>
          </li>
      </ol>
    </div>

  </div>
</template>

<script>


export default {
  name: 'Card',
  props: {
    title: String,
    id: String,
    subjects: [String],
    link: String,
    
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3.paper-title{
  color: #212121;
}

h3.paper-id{
  color: #767676;
}

li {
  display: inline-block;
}

a {
  color: #b31c1b;
}

div.card{
  width:400px;
	height:240px;
  margin-left: 30px;
  margin-right: 30px;
  margin-top: 20px;
  margin-bottom: 20px
  
 
}

div.card-header{
  /*width:330px;*/
	height:140px;
	
	/*left:20px;*/
	/*margin-right:20px;*/
	
	display:flex;
	flex-direction:column;}

div.card-content{
  display:flex;
  width:100%;
  height:65px;
  max-height:65px;
  align-items:center;
  justify-content:space-between;
  flex: 1 0 auto;
}
div.link-container{
  width:100%;
}
div p.card-content-text{
    margin:0;
    letter-spacing:1px;
  }
</style>
