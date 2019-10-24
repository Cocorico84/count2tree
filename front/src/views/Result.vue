<template>
  <v-content>
    <Tree :tree="tree" v-for="tree in trees" :key="tree.name" />
  </v-content>
</template>

<script>
import Tree from "../components/Tree";

export default {
  data: () => ({
      trees: [],
  }),
  components: {
    Tree
  },
  methods: {}
};
</script>