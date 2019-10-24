<template>
  <v-footer color="primary lighten-1" padless>
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="link in links"
        :key="link.name"
        color="white"
        text
        rounded
        class="my-2"
        :to="link.path"
        :href="link.path"
      >{{ link.name }}</v-btn>
      <v-col class="primary lighten-2 py-4 text-center white--text" cols="12">
        {{ new Date().getFullYear() }} —
        <strong>Agility Factory</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>


<script>
import router from "../router.js";
import Navbar from "../components/Navbar";

export default {
  data: () => ({
    links: [
      { name: "Home", path: "/" },
      { name: "About Us", path: "/about" },
      { name: "Team", path: "/team" },
      { name: "Contact Us", path: "/contact" }
    ]
  }),
  router: router,
  components: {
    Navbar
  },
};
</script>