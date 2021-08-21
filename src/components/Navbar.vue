<template lang="pug">
nav
  v-app-bar(flat, app, dark)
    // Title
    v-toolbar-title.text-uppercase.grey--text
      router-link(to='/')
        img(src="../assets/logo.png" v-on:click="" style="height: 55px; margin-top: 5px")
    v-spacer
    // Dark mode
    v-btn(text, icon, color='grey', @click='toggleMode')
      v-icon(small) brightness_2
    // Language picker
    v-menu(offset-y)
      template(v-slot:activator='{ on }')
        v-btn(text, icon, color='grey', v-on='on') {{ currentLocale.icon }}
      v-list
        v-list-item(
          v-for='locale in locales',
          @click='changeLanguage(locale.code)',
          :key='locale.code'
        )
          v-list-item-title {{ locale.icon }}
    v-menu(:close-on-content-click="close_overlay")
      template(v-slot:activator="{on, attrs}")
        v-btn(color='grey' icon, v-bind="attrs", v-on="on" @click="close_overlay = false")
          v-icon settings
      .v-container
        v-text-field(v-model="api_base").mt-12
        v-btn(icon @click="changeApiBase(); close_overlay = true")
          v-icon save 
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'
import { i18n } from '@/plugins/i18n'
import * as api from '@/utils/api'
import { namespace } from 'vuex-class'

const AppStore = namespace('AppStore')

@Component
export default class Navbar extends Vue {
  @AppStore.State dark!: boolean

  @AppStore.Mutation setDark!: (dark: boolean) => void
  @AppStore.Mutation setLanguage!: (language: string) => void
  @AppStore.Mutation setApiBase!: (api_base: string) => void

  api_base: string = "https://";
  close_overlay: boolean = false;

  get locales() {
    return [
      { icon: '🇺🇸', code: 'en' },
      { icon: '🇷🇺', code: 'ru' },
    ]
  }
  get currentLocale() {
    for (const locale of this.locales) {
      if (locale.code === i18n.locale) {
        return locale
      }
    }
  }

  toggleMode() {
    this.setDark(!this.dark)
    ;(this.$vuetify.theme as any).dark = this.dark
  }
  changeLanguage(locale: string) {
    i18n.locale = locale
    this.setLanguage(locale)
    document.title = i18n.t('strippedTitle') as string
  }
  changeApiBase() {
    this.setApiBase(this.api_base);
  }
}
</script>

<style>
nav a:link {
  text-decoration: none;
}

nav a:visited {
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}

nav a:active {
  text-decoration: underline;
}
</style>
