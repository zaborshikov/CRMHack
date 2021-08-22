<template lang="pug">
.v-container.pa-4.mt-12
  // Main content
  v-layout()
    v-flex(xs1, md2)
    v-flex(xs10, md8)
      span._headline.pt-4 Сервис по анализу облика компании в обществе.
      .v-container
        p.mt-12 Для того, чтобы открыть результаты анализа, введите ссылку на сообщество вконтакте
        v-layout(wrap v-on:keyup.enter="sendCompanyLink()").mt-12
          v-layout
            p.mt-2(style="display: flex; align-items: center;") vk.com/
            v-text-field(label="Ссылка", :color="color", placeholder="fmproducts", v-model="link", :loading="loading")
          v-btn(large outlined width="100" @click="sendCompanyLink()" :loading="loading" :error="btn_icon === 'mdi-close'")
            v-icon(:color="color") {{ btn_icon }}
    v-flex(xs1, md2)

</template>

<script lang="ts">
import Vue from 'vue'
import { create } from '@/utils/api'
import Component from 'vue-class-component'
import { i18n } from '@/plugins/i18n'
import { namespace } from 'vuex-class'
import { User } from '@/models/User'
import router from '@/plugins/router'

const AppStore = namespace('AppStore')
const SnackbarStore = namespace('SnackbarStore')

@Component
export default class Home extends Vue {
  @AppStore.Mutation setUser!: (user: User) => void
  @SnackbarStore.Mutation setSnackbarError!: (error: string) => void
  @AppStore.Mutation setGroupId!: (id: string) => void
  @AppStore.Mutation setGroupName!: (id: string) => void

  link: string = "";
  loading: boolean = false;
  btn_icon: string = "mdi-arrow-right";
  color: string = "none";

  async sendCompanyLink() {
    this.loading = true;
    create(this.link).then(data => {
      this.loading = false;
      this.color = "green";
      this.btn_icon = "mdi-done";
      console.log(data);
      this.setGroupId(data);
      this.setGroupName(this.link);
      this.$router.push("/dashboard");
    })
    .catch(e => {
      console.log(e);
      this.loading = false;
      this.btn_icon = "mdi-close";
      this.color = "red";
      this.delay(2000).then(() => {
        this.btn_icon = "mdi-arrow-right";
        this.color = "none";
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
