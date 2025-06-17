import kotlinx.serialization.*
import com.charleskorn.kaml.Yaml
import java.io.File

@Serializable
data class Intent(
    val intent: String,
    val examples: String
)

@Serializable
data class NLU(
    val version: String,
    val nlu: MutableList<Intent>
)

fun getInputStream(fileName: String)
        = File(fileName).inputStream()

object MyRasa {

    val nlu_file = "/home/ema/IdeaProjects/chatbot-p/rasa/data/nlu.yml"

    fun parsing(): NLU {
        val input = getInputStream(nlu_file)
        val result = Yaml.default.decodeFromStream(NLU.serializer(), input)
        return result
    }

    fun serialize(nlu: NLU) {
        val result = Yaml.default.encodeToString(NLU.serializer(), nlu)
        File(nlu_file).writeText(result)
    }

    fun add_intent(nlu: NLU) {
        println("Inserire l'intent:")
        val intent = readln()
        println("Inserire il numero di examples:")
        val n: Int = readln().toInt()
        println("Inserire gli examples:")
        var examples = ""
        for(i in 0 until n) {
            examples = examples + "- " + readln() + "\n"
        }
        val result = Intent(intent, examples)
        nlu.nlu.add(result)
    }
}
