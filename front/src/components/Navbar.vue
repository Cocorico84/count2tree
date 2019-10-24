<template>
  <nav>
    <v-app-bar flat src="../assets/arbre.jpg">
      <template>
        <v-btn class="white--text" icon to="/">
          <v-icon>home</v-icon>
        </v-btn>
      </template>
      <v-toolbar-title>
        <span class="white--text">Count2Tree</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <Search @search="searchTree" />

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" class="white--text" icon @click="clear">
            <v-icon>delete</v-icon>
          </v-btn>
        </template>
        <span>Clear search</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" class="white--text" icon @click="dialogFav = true">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
        </template>
        <span>Favorites</span>
      </v-tooltip>
      <v-dialog v-model="dialogFav" max-width="500">
        <Favorite @favorite="changeColor" />
      </v-dialog>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" class="white--text" icon @click="dialogLog = true">
            <v-icon>face</v-icon>
          </v-btn>
        </template>
        <span>Login</span>
      </v-tooltip>
      <v-dialog v-model="dialogLog" max-width="360">
        <Login />
      </v-dialog>
    </v-app-bar>

    <v-content class="brown lighten-3">
      <Tree :tree="tree" v-for="tree in trees" :key="tree.name" />
    </v-content>
    <v-card>
      <Sparkline @spark="showSparkline" />
    </v-card>
  </nav>
</template>

<script>
import axios from "axios";
import Login from "./Login";
import Search from "./Search";
import Tree from "./Tree";
import Favorite from "./Favorite";
import Sparkline from "./Sparkline";
import router from "../router.js";

export default {
  name: "Navbar",
  data: () => ({
    trees: [],
    items: [],
    value: [],
    dialogFav: false,
    dialogLog: false,
    fav: []
  }),
  router: router,

  components: {
    Login,
    Search,
    Tree,
    Favorite,
    Sparkline
  },
  methods: {
    searchTree(search) {
      let params = { query: search };
      axios
        .get("http://localhost:8000/api/v1/trees", { params: params })
        .then(response => {
          this.trees = response.data;
        });

      axios
        .get("http://localhost:8000/api/v1/locations", { params: params })
        .then(response => {
          this.items = response.data;
        });

      axios
        .get("http://localhost:8000/api/v1/height", { params: params })
        .then(response => {
          this.value = response.data;
        });
    },
    changeColor(favorite) {
      let params = { query: favorite };

      axios
        .post("http://localhost:8000/api/v1/favorite", params)
        .then(response => {
          this.fav = response.data;
        });
    },
    showSparkline(search) {
      let params = { query: search };

      axios
        .get("http://localhost:8000/api/v1/height", { params: params })
        .then(response => {
          this.value = response.data;
        });
    },
    clear() {
      Object.assign(this.$data, this.$options.data());
    }
  }
};
</script>