<template>
  <v-row>
    <v-col cols="12" sm="6" offset-sm="3">
      <v-card>
        <v-container fluid>
          <v-row>
            <v-col v-for="n in 9" :key="n" class="d-flex child-flex" cols="4">
              <v-card flat tile class="d-flex">
                <v-img
                  v-for="link in links"
                  :key="link.path"
                  :src="link.path"
                  aspect-ratio="1"
                  class="grey lighten-2"
                >
                  <template v-slot:placeholder>
                    <v-row class="fill-height ma-0" align="center" justify="center"></v-row>
                  </template>
                </v-img>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    links: [
      { path: require("../assets/arbre1.jpeg") },
      { path: require("../assets/arbre2.jpeg") },
      { path: require("../assets/arbre3.jpeg") },
      { path: require("../assets/arbre4.jpeg") },
      { path: require("../assets/arbre5.jpeg") },
      { path: require("../assets/arbre6.jpeg") },
      { path: require("../assets/arbre7.jpeg") },
      { path: require("../assets/arbre8.jpeg") },
      { path: require("../assets/arbre9.jpeg") }
    ]
  })
};
</script>