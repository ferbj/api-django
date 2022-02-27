<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light navbar-laravel">
      	<router-link class="nav-brand" to="/">
        <img class="img-responsive" width="50px" alt="logo" src="https://pbs.twimg.com/profile_images/1226898562010767360/PBYe9jgY_400x400.png"/>
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
