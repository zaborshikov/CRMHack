<template lang="pug">
.v-container.pa-4.mt-12
  // Main content
  v-layout()
    v-flex(xs1, md2)
    v-flex(xs10, md8)
      span._headline.pt-4 Сервис по анализу облика компании в обществе.
      .v-container
        p.mt-12 Для того, чтобы открыть результаты анализа, введите ссылку на сообщество вконтакте
        v-layout(wrap).mt-12
          v-text-field(label="Ссылка", placeholder="vk.com/..." v-model="link")
          v-btn(large outlined width="100")
            v-icon mdi-arrow-right
        p {{ link }}
    v-flex(xs1, md2)

</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
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
