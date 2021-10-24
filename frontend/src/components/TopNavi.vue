<template>
  <v-app-bar fixed flat text overlay-opacity	>
    <v-icon @click="$router.back()">mdi-arrow-left</v-icon>
  </v-app-bar>
</template>

<style>
  .theme--light.v-app-bar.v-toolbar.v-sheet {
    background-color: rgba(0,0,0,0);
  }
</style>