<template>
  <div class="container">
    <div id="nav">
      <Header />
    </div>
        <router-view/>
    </div>  
</template>

<style>

.navbar-laravel {
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
  }
</style>
<script>
import Header from "./views/Header";
export default {
  name: "App",
  components:  { Header }
};
</script>
