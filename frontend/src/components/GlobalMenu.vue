<template>
  <div class="mt-6">
    <img src="@/assets/top.jpeg" width="100%">
    <v-row justify="center" class="my-5 ma-5">
        <v-btn
          depressed
          color="pink darken-1"
          x-large
          block
          href="offer-form"
          class="white--text font-weight-bold body-1"
          elevation="5"
          raised
        >
          査定を依頼する
        </v-btn>
    </v-row>
  </div>
</template>

<style lang="scss" scoped>
 $pc-min: 960px;
 @mixin display_pc {
   @media (min-width: $pc-min) {
     @content;
   }
 }
 .sp-visible {
   @include display_pc {
     display: none !important;
   }
 }
</style>