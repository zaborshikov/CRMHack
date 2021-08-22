import { User } from '@/models/User'
import { VuexModule, Module, Mutation } from 'vuex-module-decorators'

@Module({ namespaced: true, name: 'AppStore' })
export default class AppStore extends VuexModule {
  user?: User = undefined
  language?: string = undefined
  dark = false
  group_id?: string = "";
  group_name?: string = "Дэшборд";
  api_base = "https://abc.def"

  @Mutation
  setUser(user?: User) {
    this.user = user
  }

  @Mutation
  setLanguage(language: string) {
    this.language = language
  }

  @Mutation
  setDark(dark: boolean) {
    this.dark = dark
  }

  @Mutation
  setApiBase(api_base: string) {
    this.api_base = api_base;
  }

  @Mutation
  setGroupId(id: string) {
    this.group_id = id;
  }

  @Mutation
  setGroupName(name: string) {
    this.group_name = name;
  }
}
