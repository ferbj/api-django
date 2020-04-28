<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light navbar-laravel">
      	<router-link class="nav-brand" to="/">
        <img class="img-responsive" width="100px" src="https://hakeema.imgix.net/co-incide/unit/5aecf7b06015d26c536ca9d6-c9c512.jpeg?w=250&h=250&fit=fillmax&bg=FFFFFFFF&pad=5&auto=format"/>
        </router-link>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupport" aria-controls="true"> 
					<span class="navbar-toggler-icon"></span>
				</button>
      <div class="collapse navbar-collapse" id="navbarSupport">
        <ul class="navbar-nav">
          
            <li class="nav-item">
              <a class="nav-link" href="/cursos">Cursos</a>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/country">Lista de poblacion a nivel mundial</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/graphics">Grafico</router-link>
            </li>
         
        </ul>
      </div>
    </nav>
  </div>
</template>
<style scoped>

</style>
<script>
export default {
  name: 'app-header',
};
</script>
