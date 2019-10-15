<template>
  <v-sheet>
    <v-sparkline
      :value="value"
      :gradient="gradients"
      :smooth="radius || false"
      :padding="padding"
      :line-width="width"
      :stroke-linecap="lineCap"
      :gradient-direction="gradientDirection"
      :fill="fill"
      :type="type"
      :auto-line-width="autoLineWidth"
      auto-draw
      :labels="value"
    ></v-sparkline>
  </v-sheet>
</template>

<script>
import axios from "axios";

const gradients = [
  ["#222"],
  ["#42b3f4"],
  ["red", "orange", "yellow"],
  ["purple", "violet"],
  ["#00c6ff", "#F0F", "#FF0"],
  ["#f72047", "#ffd200", "#1feaea"]
];

export default {
  data: () => ({
    width: 2,
    radius: 10,
    padding: 8,
    lineCap: "round",
    gradient: gradients[5],
    value: [],
    gradientDirection: "top",
    gradients,
    fill: false,
    type: "trend",
    autoLineWidth: false
  }),
  created() {
    this.searchTree();
  },
  methods: {
    searchTree() {
      axios.get("http://localhost:8000/api/v1/height").then(response => {
        this.value = response.data;
      });
    }
  }
};
</script>
