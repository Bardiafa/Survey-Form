<template>
    <div class="container is-fluid has-background-black-bis">
        <div class="columns">
            <div class="column">
                <div class="column is-2 is-offset-10">
                    <button @click="logout()" class="button is-danger">Log out</button>
                </div>
                <form @submit.prevent="submitForm">

                    <div class="content has-text-white has-text-centered">
                        <br>
                        <h1 class="title is-size-1 has-text-white">Compelete Forms</h1>
                        <p class="text is-size-4">Choose your desire teacher</p>
                        <div class="field">
                            <div class="control">
                                <div class="select is-link">
                                    <select v-model="teacher_name">
                                        <option value="Laali">Teacher Laali</option>
                                        <option value="Najafi">Teacher Najafi</option>
                                        <option value="Mansoori">Teacher Mansoori</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="columns is-gapless">
                        <div class="column is-1"></div>
                        <div class="column is-five-sixth has-text-white">
                            <br>
                            <p class="text is-size-4">Question1 : How was this teacher overall?</p>
                            <br>
                            <p class="text is-size-4">Question2 : How was this teacher on online teaching?</p>
                            <br>
                            <p class="text is-size-4">Question3 : Rate this teacher on teaching?</p>
                            <br>
                            <p class="text is-size-4">Question4 : Rate this teacher knowledge?</p>
                            <br>
                            <p class="text is-size-4">Question5 : Rate this teacher presence in online classes?</p>
                            <br>
                            <p class="text is-size-4">Question6 : Rate this teacher presence in university?</p>
                            <br>
                            <p class="text is-size-4">Question7 : Rate this teacher question answering?</p>
                            <br>
                            <p class="text is-size-4">Question8 : Rate this teacher answering Email?</p>
                        </div>

                        <div class="column is-1">
                            <div class="field">
                                <div class="control">
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q1" @change="onQ1" value="1">
                                        1
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q2" @change="onQ2" value="1">
                                        1
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q3" @change="onQ3" value="1">
                                        1
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q4" @change="onQ4" value="1">
                                        1
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q5" @change="onQ5" value="1">
                                        1
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q6" @change="onQ6" value="1">
                                        1
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q7" @change="onQ7" value="1">
                                        1
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q8" @change="onQ8" value="1">
                                        1
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="column is-1">
                            <div class="field">
                                <div class="control">
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q1" @change="onQ1" value="2">
                                        2
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q2" @change="onQ2" value="2">
                                        2
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q3" @change="onQ3" value="2">
                                        2
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q4" @change="onQ4" value="2">
                                        2
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q5" @change="onQ5" value="2">
                                        2
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q6" @change="onQ6" value="2">
                                        2
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q7" @change="onQ7" value="2">
                                        2
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q8" @change="onQ8" value="2">
                                        2
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="column is-1">
                            <div class="field">
                                <div class="control">
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q1" @change="onQ1" value="3">
                                        3
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q2" @change="onQ2" value="3">
                                        3
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q3" @change="onQ3" value="3">
                                        3
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q4" @change="onQ4" value="3">
                                        3
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q5" @change="onQ5" value="3">
                                        3
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q6" @change="onQ6" value="3">
                                        3
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q7" @change="onQ7" value="3">
                                        3
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q8" @change="onQ8" value="3">
                                        3
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="column is-1">
                            <div class="field">
                                <div class="control">
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q1" @change="onQ1" value="4">
                                        4
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q2" @change="onQ2" value="4">
                                        4
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q3" @change="onQ3" value="4">
                                        4
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q4" @change="onQ4" value="4">
                                        4
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q5" @change="onQ5" value="4">
                                        4
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q6" @change="onQ6" value="4">
                                        4
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q7" @change="onQ7" value="4">
                                        4
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q8" @change="onQ8" value="4">
                                        4
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="column is-1">
                            <div class="field">
                                <div class="control">
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q1" @change="onQ1" value="5">
                                        5
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q2" @change="onQ2" value="5">
                                        5
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q3" @change="onQ3" value="5">
                                        5
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q4" @change="onQ4" value="5">
                                        5
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q5" @change="onQ5" value="5">
                                        5
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q6" @change="onQ6" value="5">
                                        5
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q7" @change="onQ7" value="5">
                                        5
                                    </label>
                                    <br>
                                    <br>
                                    <label class="radio is-size-3">
                                        <input type="radio" name="q8" @change="onQ8" value="5">
                                        5
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <br>

                    <div class="columns iss-gapless">
                        <div class="column is-one-third">

                        </div>
                        <div class="column is-one-third">
                            <div class="notification is-danger is-fullwidth " v-if="errors.length">
                                <p class="text is-multiline" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>
                            <div class="field">
                                <div class="control ">
                                    <button class="button is-large is-link is-fullwidth">Submit</button>
                                </div>
                            </div>
                        </div>
                        <div class="column is-one-third">

                        </div>
                    </div>
                    <br>
                    <br>
                    <br>

                </form>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Register',
    data() {
        return {
            teacher_name: '',
            q1: '',
            q2: '',
            q3: '',
            q4: '',
            q5: '',
            q6: '',
            q7: '',
            q8: '',
            errors: []
        }
    },
    methods: {
        onQ1(event) {
            this.q1 = event.target.value;
            console.log(this.q1)
        },
        onQ2(event) {
            this.q2 = event.target.value;
        },
        onQ3(event) {
            this.q3 = event.target.value;
        },
        onQ4(event) {
            this.q4 = event.target.value;
        },
        onQ5(event) {
            this.q5 = event.target.value;
        },
        onQ6(event) {
            this.q6 = event.target.value;
        },
        onQ7(event) {
            this.q7 = event.target.value;
        },
        onQ8(event) {
            this.q8 = event.target.value;
        },
        async submitForm() {
            this.errors.splice(0)

            if (this.q1 === '' || this.q2 === '' || this.q3 === '' || this.q4 === '' || this.q5 === '' || this.q6 === '' || this.q7 === '' || this.q8 === '') {
                this.errors.push('Fill all questions')
            }

            if (this.teacher_name === '') {
                this.errors.push('Select your teacher')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                const formData = {
                    teacher_name: this.teacher_name,
                    q1: this.q1,
                    q2: this.q2,
                    q3: this.q3,
                    q4: this.q4,
                    q5: this.q5,
                    q6: this.q6,
                    q7: this.q7,
                    q8: this.q8,
                }

                await axios
                    .post('/api/v1/forms/', formData)
                    .then(response => {
                        toast({
                            message: 'Form Submited',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })
                        this.$router.push('/forms')
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
        },
        async logout() {
            await axios
                .post('/api/v1/token/logout')
                .then(responce => {
                    console.log('logged out')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>