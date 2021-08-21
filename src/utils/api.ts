import store from '@/store'
import axios from 'axios'
import { User } from '@/models/User'
import { namespace } from 'vuex-class'

// const AppStore = namespace('AppStore')
// let AppStore.State api_base!: string;

//TODO: test this

export async function create(link: string) {
  // console.log(store.state.AppStore.api_base);
  return (
    await axios.post(
      `${store.state.AppStore.api_base}/create`,
      {"vk_link": link},
    )
  ).data
}

function getHeaders(user: User) {
  if (user.token) {
    return { token: user.token }
  } else {
    return undefined
  }
}
