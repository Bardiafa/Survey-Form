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
                            <input type="email" name="email" class="input is-large is-link has-background-black has-text-white is-fullwidth" v-model="email" 
                            placeholder="Email">
                        </div>
                    </div>
                    <div class="field">
                        
                        <div class="control">
                            <input type="password" name="password1" class="input is-large is-link has-background-black has-text-white is-fullwidth" v-model="password1" 
                            placeholder="Password">
                        </div>
                    </div>
                    <div class="field">
                        
                        <div class="control">
                            <input type="password" name="password2" class="input is-large is-link has-background-black has-text-white is-fullwidth" v-model="password2" 
                            placeholder="Confirm Password">
                        </div>
                    </div>
                    <br>
                    <div class="notification is-danger is-fullwidth " v-if="errors.length">
                        <p class="text is-multiline" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <br>
                    <div class="field">
                        <div class="control">
                            <button class="button is-large is-link is-fullwidth">Register</button>
                        </div>
                    </div>
                    <br>
                    <div class="content has-text-centered">
                        <router-link to="/" class="text is-size-3 "><strong>Already have account?</strong></router-link>
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
    import {toast} from 'bulma-toast'

    export default{
        name: 'Register',
        data() {
            return{
                username: '',
                password1: '',
                password2: '',
                email: '',
                errors: []
            }
        },
        methods:{
            async submitForm() {
                this.errors.splice(0)

                if(this.username===''){
                    this.errors.push('The username is missing')
                }

                if(this.password1===''){
                    this.errors.push('The password is too short')
                }

                if(this.password1!==this.password2){
                    this.errors.push('The passwords are not matching')
                }

                if(!this.errors.length){
                    this.$store.commit('setIsLoading', true)

                    const formData = {
                        username: this.username,
                        password: this.password1,
                        email: this.email
                    }

                    await axios
                        .post('/api/v1/users/',formData)
                        .then(response => {
                            toast({
                                message: 'Account was created, please login',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right'
                            })
                            this.$router.push('/')
                        })
                        .catch(error => {
                            if(error.response) {
                                for(const property in error.response.data){
                                    this.errors.push(`${property}:${error.response.data[property]}`)
                                }
                            }else if (error.message) {
                                this.errors.push('something went wrong. Please try again!')
                            }
                        })
                    this.$store.commit('setIsLoading', false)
                }
            }
        }
    }
</script>