<template>
  <v-container>
    <v-layout v-if="tree !== null">
      <v-flex xs6>
        <v-card color="#C5E1A5" class="mx-auto">
          <v-card-title>{{ tree.genus }} {{ tree.specie }} {{ tree.variety }}</v-card-title>
          <v-card-text>{{ tree.location }}</v-card-text>
          <v-card-text>Hauteur : {{ tree.height }} m</v-card-text>
          <v-col class="text-right">
            <v-btn text icon :color="color" @click.once="change_color">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-col>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  props: ["tree"],
  data: () => ({
    color: "grey",
    fav: [],
    name: ""
  }),
  methods: {
    change_color() {
      this.color = "pink";

      let params = { query: this.change_color };
      axios
        .post("http://localhost:8000/api/v1/favorite", { params: params })
        .then(response => {
          this.selected = response.data;
        });
      console.log("Ajout d'un favori");
    }
  }
};
</script>