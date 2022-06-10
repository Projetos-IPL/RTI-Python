import cmd
import requests

API_URL = "https://rti-api.afonsosantos.me/api/"


class CmdInterface(cmd.Cmd):
    intro = 'RTI - Sistema de Segurança\nEscreva help ou ? para os comandos disponíveis.\n'
    prompt = '>>> '

    @staticmethod
    def do_portas(self):
        """Abre/fecha as portas do cenário de testes."""
        res = requests.post(
            API_URL + "eventos.php",
            json={"event_name": "OPEN_DOORS", "action": "ADD"},
            headers={"X-Auth-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                                     ".eyJ1c2VybmFtZSI6ImlvdCIsInRpbWVzdGFtcCI6MTY1MzY0NjI0N30"
                                     ".HpafidXvLMIUuHdfE9B2Gwds_iwMIzWALm8O5IHgZZA"}
        )

        if res.ok:
            print("Evento adicionado!\n")
        else:
            print("Ocorreu um erro: " + res.text + "\n")

    @staticmethod
    def do_luzes(self):
        """Acende/apaga as luzes do cenário de testes."""
        res = requests.post(
            API_URL + "eventos.php",
            json={"event_name": "TOGGLE_LIGHTS", "action": "ADD"},
            headers={"X-Auth-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                                     ".eyJ1c2VybmFtZSI6ImlvdCIsInRpbWVzdGFtcCI6MTY1MzY0NjI0N30"
                                     ".HpafidXvLMIUuHdfE9B2Gwds_iwMIzWALm8O5IHgZZA"}
        )

        if res.ok:
            print("Evento adicionado!\n")
        else:
            print("Ocorreu um erro: " + res.text + "\n")

    @staticmethod
    def do_sair(self):
        """Sair do programa."""
        exit()


if __name__ == '__main__':
    CmdInterface().cmdloop()
