import Vue from 'vue'
import Vuetify, {
  VApp,
  VAppBar,
  VToolbarTitle,
  VSpacer,
  VBtn,
  VIcon,
  VMenu,
  VList,
  VListItem,
  VListItemTitle,
  VFlex,
  VLayout,
  VSnackbar,
  VTextField,
  VTextarea,
  VInput,
  VProgressCircular,
  VSelect,
  VBtnToggle,
  VMain,
} from 'vuetify/lib'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify, {
  components: {
    VApp,
    VAppBar,
    VToolbarTitle,
    VSpacer,
    VBtn,
    VIcon,
    VMenu,
    VList,
    VListItem,
    VListItemTitle,
    VFlex,
    VLayout,
    VSnackbar,
    VTextField,
    VTextarea,
    VInput,
    VProgressCircular,
    VSelect,
    VBtnToggle,
    VMain,
  },
})

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
})
