<template>
  <v-app>
    <Navbar />
    <v-content class="brown lighten-3">
      <router-view></router-view>
    </v-content>
    <Footer />
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import router from "./router.js";

export default {
  name: "App",
  data: () => ({}),
  components: {
    Navbar,
    Footer
  },
  router: router
};
</script>