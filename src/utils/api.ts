import axios from 'axios'
import { User } from '@/models/User'

let base = 'https://template.com'

export async function reset(user: User) {
  return (
    await axios.post(
      `${base}/users/reset`,
      {},
      {
        headers: getHeaders(user),
      }
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
