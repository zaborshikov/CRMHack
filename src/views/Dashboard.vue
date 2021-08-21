<template lang="pug">
.v-container.pa-4.mt-12
  // Main content
  v-layout()
    v-flex(xs1, md2)
    v-flex(xs10, md8)
      span._headline.pt-4 Дэшборд
      v-layout(v-if="typeof $store.state.AppStore.group_id !== 'undefined'")
        span yeah
      v-layout(v-else) 
        span Что-то пошло не так. Попробуйте начать сначала. 
    v-flex(xs1, md2)

</template>

<script lang="ts">
import Vue from 'vue'
import { create } from '@/utils/api'
import Component from 'vue-class-component'
import { i18n } from '@/plugins/i18n'
import { namespace } from 'vuex-class'
import { User } from '@/models/User'

const AppStore = namespace('AppStore')
const SnackbarStore = namespace('SnackbarStore')

@Component
export default class Home extends Vue {
  @AppStore.Mutation setUser!: (user: User) => void
  @SnackbarStore.Mutation setSnackbarError!: (error: string) => void
  link: string = "";
  loading: boolean = false;
  btn_icon: string = "mdi-arrow-right";
  color: string = "black";

  async sendCompanyLink() {
    this.loading = true;
    create(this.link).then(() => {
      this.loading = false;
      this.color = "green";
      this.btn_icon = "mdi-done";
    })
    .catch(e => {
      console.log(e);
      this.loading = false;
      this.btn_icon = "mdi-close";
      this.color = "red";
      this.delay(2000).then(() => {
        this.btn_icon = "mdi-arrow-right";
        this.color = "black";
      })
    })
  }
  
  async delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
  }

}
</script>

<style>
._headline {
  font-size: 3em!important;
  font-family: 'Inter';
  font-weight: 800;
  line-height: 85%;
}
</style>
