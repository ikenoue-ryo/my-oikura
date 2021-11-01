import Vue from "vue";
import Vuetify, { colors } from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#D81B60",
        secondary: colors.green,
        accent: colors.red.darken3,
        error: colors.red,
        warning: colors.yellow,
        info: colors.grey,
        black: colors.black,
        default: "#e0e0e0",
      },
      dark: {
        primary: "#D81B60",
        secondary: colors.green,
      },
    },
  },
});