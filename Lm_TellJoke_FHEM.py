from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Lm_TellJoke_FHEM(AliceSkill):
	"""
	Author: milode
	Description: Tells joke, erzaehlt eine Witz (ueber FHEM)
	"""

	@IntentHandler('TellJoke')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
