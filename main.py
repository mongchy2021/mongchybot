import discord
import datetime


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("mongchy bot is ready!")
    print("=====================")
    game = discord.Game("mongchy!")
    await client.change_presence(status=discord.Status.idle, activity=game)

    @client.event
    async def on_message(message):
        if message.content.startswith("ㅎㅇ"):
            await message.channel.send("안녕하세요")
        if message.content.startswith("!krlevel"):
            await message.channel.send("```1. Ketthe 2. PAHEXA 3. Ankaid 4. Command_Man 5. TheCuteHax 6. firstplacehunter 7. Kenil"
                                       "8. Ribess 9. Muys 10. baazi 11. Disone 12. Motthe 13. GGungPig 14. Clorless 15. saltzrosel"
                                       "16. _GTG 17. Akyyyyyyyyys 18. immachool 19. iQuQ 20. victorypark 21. Merrykawai 22. JJoMaNi 23. tkstka 24. kugumlegend"
                                       "25. ohPau 26. Silverraptor181 27. SeongAH 28. SweetMaanngo 29. fishcookies 30. Capea 31. Pisicut 32. wkwmd 33. Vinxeen 34. KKWA"
                                       "35. NotGak 36. Lazto 37. NotAntikb 38. prelcne 39. SSmoker 40. Dqto 41. junlego 42. ThighLoverkiyn 43. NotMixu 44. dlakxm"
                                       "45. 5DENG 46. hyedoll 47. 9eb 48. 2ero 49. Wa1ker 50. SetShot```")

        if message.content.startswith("!청소"):
            number = int(message.content.split(" ")[1])
            await message.delete()
            await message.channel.purge(limit=number)
            await message.channel.send(f"{number}개의 메시지를 삭제 했습니다.")

        if message.content.startswith("?제작자"):
            await message.channel.send("mongchy#4042 (버그 문의도 여기로)")

        if message.content.startswith("!루밀잘생김"):
            await message.channel.send("뭔가 심히 잘못 됨")

        if message.content.startswith("!봇초대"):
            await message.channel.send("https://discord.com/oauth2/authorize?client_id=776980097952907314&scope=bot")
        if message.content.startswith("!내정보"):
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="닉네임", value=message.author.name, inline=True)
            embed.add_field(name="서버닉", value=message.author.display_name, inline=True)
            embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
            embed.add_field(name="ID", value=message.author.id, inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=embed)

        if message.content.startswith("!?도움말"):
            embed = discord.Embed(title="몽치봇 도움말", description="도움말", color=0xAAFFFF)
            embed.add_field(name="!krlevel", value="한국 베드워즈 50등까지 리더보드를 보여줍니다.", inline=False)
            embed.add_field(name="!청소 [값]", value="값의 수 만큼 채팅을 지워줍니다.", inline=False)
            embed.add_field(name="?제작자", value="제작자를 알려줍니다.", inline=False)
            embed.add_field(name="!봇초대", value="몽치봇 초대링크를 보여줍니다.", inline=False)
            embed.add_field(name="!내정보", value="자신의 정보를 알려줍니다.", inline=False)
            embed.add_field(name="!투표 [값]/[값]", value="투표를 합니다.", inline=False)
            embed.set_footer(text="made by mongchy")
            embed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=embed)

        if message.content.startswith("!투표"):
            vote = message.content[4:].split("/")
            await message.channel.send("⭐투표⭐ - " + vote[0])
            for i in range(1, len(vote)):
                choose = await message.channel.send("```" + vote[i] + "```")
                await choose.add_reaction('👍')

        if message.content.startswith("슈즈"):
            await message.channel.send("시그마 쟁이")

        



client.run("Nzc2OTgwMDk3OTUyOTA3MzE0.X68xGg.sPWhPNgnOUN9EdqtlnHKY01h_Jg")