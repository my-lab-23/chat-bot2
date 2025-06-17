package com.example.speak

import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.features.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import java.net.ConnectException

object MyHTTP {
    val client = HttpClient() {
        /*install(Auth) {
            basic {
                //sendWithoutRequest = true
                username = ""
                password = ""
            }
        }*/
    }

    suspend fun post(body_content: String): String {
        try {
            val url = "http://192.168.1.196:5005/webhooks/rest/webhook"
            val response: HttpResponse = client.post(url) {
                headers {
                    append("content-type", "application/json")
                }
                body = body_content
            }
            val stringBody: String = response.receive()
            return stringBody
        } catch (e: ServerResponseException) {
            return "ClientRequestException"
        } catch (e: ServerResponseException) {
            return "ServerResponseException"
        } catch (e: ConnectException) {
            return "ConnectException"
        }
    }
}
