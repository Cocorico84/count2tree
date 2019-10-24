<template>
  <v-container>
    <v-card class="pa-2">
      <v-toolbar color="teal" dark>
        <v-toolbar-title>Favorites</v-toolbar-title>
        <div class="flex-grow-1"></div>
        <v-btn icon>
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </v-toolbar>

      <v-card-text>
        <v-row v-for="n in selected" :key="n">
          <v-checkbox :label="n"></v-checkbox>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    selected: ["A", "B", "C"]
  }),
  components: {},
  methods: {}
};
</script>

