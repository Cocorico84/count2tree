<template>
  <v-content>
    <h1 
    class="pa-12 ma-12 text-center green lighten-1 display-3 font-weight-bold">The Team</h1>

    <v-card class="mx-auto" max-width="434" outlined>
      <v-col cols="6">
        <v-row>
          <v-list-item>
            <v-list-item-avatar class="profile" color="grey" size="164" tile>
              <v-img src="../assets/coco.png"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">Corentin</v-list-item-title>
              <v-list-item-subtitle>Lack of sens of humor but nice</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-row>
      </v-col>
    </v-card>

    <v-card class="mx-auto" max-width="434" outlined>
      <v-col cols="6">
        <v-row>
          <v-list-item>
            <v-list-item-avatar class="profile" color="grey" size="164" tile>
              <v-img src="../assets/aless.png"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">Alessandro</v-list-item-title>
              <v-list-item-subtitle>Geek and funny ... sometimes</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-row>
      </v-col>
    </v-card>

  </v-content>
</template>

<script>
export default {
  name: "Team"
};
</script>