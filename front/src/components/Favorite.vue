<template>
  <v-container>
    <v-layout>
      <v-flex xs8>
        <v-card max-width="475" class="pa-2">
          <v-toolbar color="teal" dark>
            <v-toolbar-title>Favorites</v-toolbar-title>
            <div class="flex-grow-1"></div>
            <v-btn icon>
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </v-toolbar>
          <v-list>
            <v-list-item-group multiple active-class>
              <v-list-item>
                <template v-slot:default="{ active }">
                  <v-list-item-action>
                    <v-checkbox v-model="active"></v-checkbox>
                  </v-list-item-action>
                  <v-list-item-content>
                    <v-list-item-title>Notifications</v-list-item-title>
                  </v-list-item-content>
                </template>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    selected: []
  })
};
</script>

