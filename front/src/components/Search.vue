<template>
  <v-toolbar-title class="mx-5 my-auto">
    <v-layout class="mx-5">
      <v-flex xs10>
        <v-select
          ref="form"
          clearable
          solo
          label="Search by location"
          :items="items"
          prepend-inner-icon="mdi-magnify"
          v-model="search"
        >></v-select>
      </v-flex>
      <v-flex xs2 class="ml-2 mt-1">
        <v-btn block large @click="searchTree" href="/result" to="/result">Search</v-btn>
      </v-flex>
    </v-layout>
  </v-toolbar-title>
</template>

<script>
import axios from "axios";
import router from "../router.js";

export default {
  router: router,
  data: () => ({
    search: "",
    items: []
  }),
  created() {
    this.searchTree();
  },
  methods: {
    searchTree() {
      axios.get("http://localhost:8000/api/v1/locations").then(response => {
        this.items = response.data;
      });

      this.$emit("search", this.search);
    }
  }
};
</script>