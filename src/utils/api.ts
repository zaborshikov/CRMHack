import store from '@/store'
import axios from 'axios'
import { User } from '@/models/User'

export async function create(link: string) {
  // console.log(store.state.AppStore.api_base);
  return (
    await axios.post(
      `${getApiBase()}/create`,
      {"vk_link": link},
    )
  ).data
}

function getApiBase() {
  return (store as any).state.AppStore.api_base;
}

function getHeaders(user: User) {
  if (user.token) {
    return { token: user.token }
  } else {
    return undefined
  }
}
