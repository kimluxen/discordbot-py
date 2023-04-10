import discord
from discord import app_commands 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f'{self.user}이 시작되었습니다')  #  봇이 시작하였을때 터미널에 뜨는 말
        game = discord.Game('TVPL 관리')          # ~~ 하는중
        await self.change_presence(status=discord.Status.idle, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name = '안녕', description='인사를 한답니다!') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"안녕하세요!", ephemeral = True) 

@tree.command(name = '문의', description = '봇을 통해 문의를 할 수 있습니다')  # 문의 명령어
async def slash2(interaction: discord.Interaction, 문의: str):  # 옵션

    
    embed = discord.Embed(title="📑 봇 문의 📑", description="ㅤ", color=0x4000FF)  # 문의 보낸 후 결과 임베드
    embed.add_field(name="봇 문의가 접수되었습니다", value="ㅤ", inline=False)
    embed.add_field(name="문의 내용", value="\n{}\n".format(문의), inline=False)  # 문의 내용
    embed.add_field(name="ㅤ", value="**▣ 문의 내용에 대한 답장은 관리자가 확인후\n24시간 내에 답장이 오니 기다려 주시면 감사하겠습니다**", inline=False) 
    embed.add_field(name="ㅤ", value="- **관리자 이름** -", inline=False)  # 관리자 이름 

    await interaction.response.send_message(embed=embed,ephemeral = True)
    
    



    users = await client.fetch_user("1060333059511169056")   # 문의 온 문의 내용을 DM으로 받을 사람의 ID
    await users.send("유저 아이디 {}  / 문의 내용 {}".format(interaction.user.id, 문의)) # 그 사람에게 올 유저 ID와 문의 내용





@tree.command(name = '문의답변', description = '봇을 통해 문의에 답변을 할 수 있습니다') #답변하기
async def slash2(interaction: discord.Interaction, 아이디: str, 답변: str):   # 옵션

    embed = discord.Embed(title="📑 봇 답변 📑", description="ㅤ", color=0x4000FF)   # 답변 임베드
    embed.add_field(name="문의에 대한 답변 내용", value="{}".format(답변) , inline=False)   



    await interaction.response.send_message(f"✅ **답변이 완료되었습니다.**", ephemeral = True)  # 보내졌을시 나오는 확인 이모티콘


    user = await client.fetch_user("{}".format(아이디))
    await user.send(embed=embed)

client.run('MTA5NDg5MTcxNjk5OTM5MzM0MA.G0SrjW.3ShYteiYjTxJddoaY8v4lVD65bnewn-KSA0KOE')
