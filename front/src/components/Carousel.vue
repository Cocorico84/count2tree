<template>
  <v-carousel :show-arrows="false" :cycle="true">
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
      reverse-transition="fade-transition"
      transition="fade-transition"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        src: require("../assets/slide1.jpg")
      },
      {
        src: require("../assets/slide2.jpg")
      },
      {
        src: require("../assets/slide3.jpg")
      },
      {
        src: require("../assets/slide4.jpg")
      },
      {
        src: require("../assets/slide5.jpg")
      }
    ]
  })
};
</script>