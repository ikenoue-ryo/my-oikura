<template>
  <div>
    <v-container>
      <img src="@/assets/main.png" width="100%">
      <v-row justify="center" class="my-10 ma-1">
          <v-btn
            depressed
            color="primary"
            x-large
            block
            href="offer-form"
          >
            査定を依頼する
          </v-btn>
      </v-row>

    <!-- <v-app-bar flat>
      <v-toolbar-items>
        <v-btn text :to="`/`" width="150">トップ</v-btn>
        <v-btn text :to="`/offer-form/`" width="150">査定依頼</v-btn>
        <v-btn text :to="`/client-shop-search`" width="150">店舗を探す</v-btn>
        <v-btn text :to="`/car-search`" width="150">相場を見る</v-btn>
      </v-toolbar-items>
    </v-app-bar> -->
    </v-container>

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