<template>
    <div class="container is-fluid">
        <div class="columns is-gapless is-desktop">
            <div class="column is-1 has-background-black-bis is-narrow"></div>
            <div class="column is-1 has-background-black-bis is-narrow"></div>
            <div class="column is-one-sixth has-background-black-bis is-narrow">
                <div class="has-text-white">
                    <br>
                    <br>
                    <br>
                    <br>
                    <h1 class="title is-size-1 has-text-white">Login</h1>
                    <p class="text is-size-4">Welcome, Friend!</p>
                    <br>
                    <br>
                </div>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        
                        <div class="control">
                            <input type="number" name="username" class="input is-large is-link has-background-black has-text-white is-fullwidth" v-model="username" 
                            placeholder="Uni Number">
                        </div>
                    </div>
                    <div class="field">
                        
                        <div class="control">
                            <input type="password" name="password" class="input is-large is-link has-background-black has-text-white is-fullwidth" v-model="password" 
                            placeholder="Password">
                        </div>
                    </div>
                    <br>
                    <div class="notification is-danger is-fullwidth " v-if="errors.length">
                        <p class="text is-multiline" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <br>
                    <div class="field">
                        <div class="control">
                            <button class="button is-large is-link is-fullwidth">Login</button>
                        </div>
                    </div>
                    <br>
                    <div class="content has-text-centered">
                        <router-link to="/register" class="text is-size-3 "><strong>Not a User? Signup</strong></router-link>
                    </div>
                </form>
            </div>
            <div class="column is-1 has-background-black-bis is-narrow"></div>
            <div class="column is-1 has-background-black-bis is-narrow"></div>

            <div class="column is-half">
                <figure class="image is-fullwidth">
                    <img src="../../public/half.png">
                </figure>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors.splice(0)

            this.$store.commit('setIsLoading', true)

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post('/api/v1/token/login/', formData)
                .then(response => {

                    
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    

                    axios.defaults.headers.common['Authorization'] = 'Token ' + token

                    localStorage.setItem('token', token)
                    this.$router.push('/form')
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}:${error.response.data[property]}`)
                        }
                    } else if (error.message) {
                        this.errors.push('something went wrong. Please try again!')
                    }
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>