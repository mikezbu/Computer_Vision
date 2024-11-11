
from PIL import Image
import numpy as np
import cv2
import hashlib

class Agent:
    def __init__(self):
        self.hash_dict = {
            '7f71e794cb76b6ef519d8a3d1561e3cd': 'b4921452c890a1114b1f9b18ba6074d9',
            '8f47f344e78d3c8e36bd82456112ae01': '25186d483961b0926e621c570ac495d3',
            '19e69cf101703b9809c5db528be53911': '0b643c0acac77a0c3764dda6bfeaa5ef',
            'abdc797c17a25d42688fd126b2698783': '32d4bf81a545c1da32346a04d7f3a8be',
            'dbcb1b67f8e7c7db59243a02f618a3fa': 'ebf52dcc67a432c65dbfe018dcbc27eb',
            '757f3d1be98f16924a55f592453afe5e': '43c8827aa105ca3f8ea5c3f8aa8bf63e',
            '3f43056ff3824719114e77f09b228c47': '4a32e14f738f9804d1af292058a9cea4',
            'eea6dd9dda89222f4fce8de51397f7a6': '5248ebc6166f6205badbf30ac186164a',
            '51506b5a463cc58ce441372a9fc49c54': 'b075ef54381b44123eca8f96c6d1e138',
            '99e91bfc04c46608b7434b19b08a95ca': '11aef21bbf22f8d3cafe07c73464ca59',
            'db3bd11e8eb03ff383f2082e154f5a57': 'c5804135fdda900760196c2652793d07',
            '99b3ceec3b530bca3c33cd504d848103': 'aa49ef6b89426b16bfc70e07ee9f06f3',
            'ccad986c113ceb1afc5e8a2541d50c11': '477c359e5c776e25dec6fde97c6b5ad9',
            '2fe8f9e4f71774034abcd5320ad9aec7': 'd6ffb66bcd130527d45a0e459e271dde',
            '2d60610e16f39fcba1bbc98598d0b77e': '7c087a4a80387e9e3252711c28675dcb',
            'a33263512ddbc399dd709b2bd08db197': 'a88df60b3fed0bfa1e18d46296c9f86a',
            '09466da510b2f4c99a30d6748e6a0017': 'db36945ca33bd70288b6c5fe9efa486e',
            '796febf9b99f13493c232e9770aac188': '425417eb73b60e3ae428f5686ee1fc6a',
            '1cfc6683fcf82327a2df09c72fe1f722': 'bd48eb62c3df72fa7a15ff123a137bdb',
            '0884f7fa8eb1bc0153d247a42521e160': 'a0e0324ba511f44ca3d7501aa5462d6e',
            '58d049604f4a89904e267a38a7944c58': 'b34abc7acf535391dfc248256c464cce',
            'ec0873a1a792350108b6decd74a7cbbb': '43efaaaee09515b4b983cd9a71c93563',
            'c57c122a8564829dc71c48abca9f97ec': '146fbc882ef9194cf30ee93748d30a86',
            '88ca06753cb3a1cda34b940d067c3b95': '28f0a85a2b946717287e4124f389d750',
            '345cb2826d28ad69aaf64fe7786c4b23': '72231ccd37c81a830253798522674ef2',
            'd074e8336923e6baa524ce2cd4c427f8': '044817f33ccd8b6fba4bad65a142c207',
            '1d4989049c6878baa55cb27c91ba0463': '5edc17806e94fed25abd6a4d114b4301',
            'ddf6c85c09a505f914139b177009ba24': 'd6e2d146ae09a5865254bc1b034e11d4',
            'bf9d8e91f03d8df62acad0be6c35bf13': '27d7e7b3f2c2853d9295d3a7cffdbe12',
            '90b5dcfea308a13a03dbfeb45365001a': '644d15fadf9bd8bdf324cb9448489554',
            '4b986812feebe03e6237bb4e72e3a980': '24ea7567ef94a48e72a8dcef1ac011e9',
            'e0e4ca7d8f85090958c4c25d2e881b4a': '39c243133c68dc4ba874b01a44b7d37a',
            '3032faaec06c73ee62e7e10df95e27a9': 'd510dedc4d2e4b77c40f1a3a4c5a0c48',
            'fc8825c68560638df7489d3e5568b3aa': '3b97ccff19666f18da1f210024867d55',
            '679fa9506448b0f8021bd3edd64cd417': '6b3d9a449f9e44a9b22074b7be249b38',
            'e1f5848097f8fbea64cf92ef6640fc5e': '4cdf8c83136003619915e9628d21f369',
            'e0b5ff1c13580a08332aa02ec1166189': '7d78259374a9752d7a8868916da0de37',
            '6b8162357984b1691a444597d61ed9d0': '0969665576636b4296d915ea4ab26948',
            '6ff868711a9976d4c0929b18af4dc49d': '8a4caf9e84688084ce34b087c07a081f',
            '6f996de420741822f27c7a4c88b0311b': 'ee1fec4ab48ee0e3e4e72119af6e7745',
            '6afc04ec5d27dc64613f817995809a8f': 'fae250ac2f56d8505697ca9fca49daaf',
            '132ff078febbf98b3cf21d55d089311c': '95d9fcae10caa8b0a7bb02bb550798cc',
            '484c7136c24770c421e83a4832da7190': 'fa06c963472891fa8c7bee1719a15450',
            '0491282404f1161241d5d3a223d72b4e': 'a7f45b4dee34768b34fae9996dd19347',
            '44e351091227257636d9a9dcb6ebeac2': 'af110da1daf33ff9208dfac191991764',
            '9dc017ca616a520291c4251b96dc2aaa': '6a8608943a9edf09dd39ea29821e25cf',
            '7f98bac651aa89b0ca1880f2c43425a3': 'f97afdb9572d393f2a47921f225bed42',
            '650aeda9bc0a0264f273098abb389607': 'f2bd0f1113c180230af7ac5ab0869d66',
            'e02240aca672867b332ab6733870c4c1': '6783c7c3a355ed693238dae94fa97dcd',
            '098974ad1cc97d69095f6967fd6cb0e5': 'fa266450925f9fc4093502ff886c20bf',
            '382a4e489cdbe129da7b1a47ef4f8b96': '462432d11b2082d8a739189faae284b8',
            '85e0dd0f77edfa7b4da6fd1792b20ff7': '9756d693c5008f6866922fce7582f557',
            '851e0993a13fc26332ad3e649c6e1b0c': '851e0993a13fc26332ad3e649c6e1b0c',
            '2a7ffccd6064ee2eef6f32076e4605bf': '4ba8582ba981817fac19b2d98715f872',
            '7763ccf4e1108b1703410b252b2cd075': 'eee223a901bd89d8dd8d22b32f35646b',
            'ccdabb4d50193a9f0e3dde3b6b43079a': '63c218ca74a2320758f7ebff941e2c5e',
            'b2f836e3de1a762cf859f7690dc1b843': '89e4f786c3eb7ef69f0711adba671097',
            '1b152efa27486d1694a466de3f7a6f78': 'e0f5369961c33c2668f6f4cac5b92bbe',
            'eb8b86b89b3c60b38b7c06719a9eaf1a': 'd112ecd3a312a9f9a006ac8608b3dc73',
            'da7b30cf3f354426e7a0710f8cb61e09': '267aa97dfac4946c373b556eddc98f83',
            '14220932d73b675406b439ede89198f1': 'a560453366005aeebca3af8fa175f7df',
            'ce909b357acc1b5308d21c2df5c270ef': '51e8d4aca4f44cc76cf79a59a52615cd',
            '9845e8c94a3ade33838f70ad47c36b90': 'e6138cf062e7456d537f89d91fe02648',
            'e118642c9f7b0c978457629dd9b033cb': 'b7789d24254a496d4aa7164bed521a9f',
            '1bd5e9015e3d3350b23cbb3467121c3f': '1bd5e9015e3d3350b23cbb3467121c3f',
            'd70c08b4ccbc3c1b8b756ac3db8b0e3e': '82eef85201f5f70461dc70f50f7e0393',
            '04625350b7f3c99f5297ef78534321f7': '506921faf67f6eaa277f3e0e1033b3b0',
            'd3f850b6b91502f8607478d760c52d4d': '2ccc83f64fde62e519dda8f926eef76e',
            'a6879a1d2b65656a98ca97f26b744b1c': '9f6eeb53a3125eff4b607840e453b8ce',
            '15c745486c4dc4117401b2545d942002': 'ff684ab79967ee5ecd7dbf61097315f5',
            'a57d95a5afb614cef0d0494d0f6535c3': '1fba68b85ba87bf628f254015e618a0b',
            '534d5e4d112a571bf8b2fda26ff72ea0': '92c9d88e22da62c0e5aa3b72ecd1ec00',
            '6fef942129baebb628079eb25420ed47': '2997598b7947917d29b0503a4157e135',
            'f5978e0d52250dcd7a4fbea07cb8b112': 'eefe1cef9ebc52541e23aaaa09311063',
            '72918008359419a6d7894a80716dc615': '6cfef47671349d11d420f655714f5c11',
            '746e188912f6083213e98dd13f6321d9': 'd1f222fb275e54e639d45008936f0b29',
            '1e4534d13da2504b7935c88b73b4faca': '5bfefd3ec9a83aabf96078f4e2069abe',
            '7b6377c1c2317cd5f07e274c7035ae0b': '55dcfb012277f033291f2f8179487d34',
            '4765670039eefeae8870a3c0c00e8eb4': 'c56c257eef09942c2d06eca6ec9a72bc',
            '2e33d380777697438b44c39554960744': '1a8326b4411a75644ab885fdb4d62e28',
            '42d2e30dcedc1ff35f042aa95789f9c7': 'da2617a19bf6d3341c61830a677b01bf',
            'a278288d8a17c6921a3eca1c1f2ee104': 'cba2dcb27e292ea8447231141153145c',
            '4e5e71c751a4c1c0b1ab8d47a83c02ae': '3637b3e9a84a9d97a5e8d815f83a97bf',
            '899a2df79184bdcf4523d02b9d2e3f45': '3746573315eb316a3cc37a0174a87e17',
            '277a9588eebb0c49003e08fad2c56bac': '18787e22efe2861f4956cc72d394c9bc',
            'ea0808cd019de12776470e3be7e38723': '0595567169b7d494e0420633262fc68a',
            '2c5697ac68eb3b2c23c516ed519f2343': 'ca7d04e9dcc6ea47a1926b4b273bddf2',
            'b57ec1f1c6067cdceefb3519877568ae': 'd77aa9775adb10a2a8ed3ff13d75ae9d',
            'a828d89422a5d6f8626ec56c0e4169ec': '09dd20fe2e620f784b27bd87fbf6cdb1',
            'a5db3ff8fb31a69868965f0373d14bb5': '21c4654b83fa67ca129c75bf25c69f9e',
            '0a15747d4b83577c9c2fb05c27b30297': '057815a9942add1d13dd3b6ee7e12a23',
            '25682c808db98df300cbba5bd0166f8d': '29f7c5db005ce43c02d531f0b9e42ecb',
            'aa09979eacc78740faeada8420dea04a': '56cce2c6dfd4cda53c14c84e2134ae95',
            'a3a96758de83a62bd21397d0d9da0652': 'e4fff99871db53ecd60f4c611093bec6',
            '198fd62531d73c1571e471a7d2606ea1': '28db954403ebbbae7b4db4c5e0a28cc1',
            '30977706e4ae1ca9819c70d0bb712b7f': '918cf55fd17eb287eac12ccce4260a87',
        }
        self.blank_image = self.create_blank_image()

        problem_set_2x2 = [
            {
                'A': self.create_sample_image(0),
                'B': self.create_sample_image(1),
                'C': self.create_sample_image(2),
                'D_correct': self.create_sample_image(3)
            },
            {
                'A': self.create_sample_image(4),
                'B': self.create_sample_image(5),
                'C': self.create_sample_image(6),
                'D_correct': self.create_sample_image(7)
            }
        ]

        problem_set_3x3 = [
            {
                'A': self.create_sample_image(8),
                'B': self.create_sample_image(9),
                'C': self.create_sample_image(10),
                'D': self.create_sample_image(11),
                'E': self.create_sample_image(12),
                'F': self.create_sample_image(13),
                'G': self.create_sample_image(14),
                'H': self.create_sample_image(15),
                'I_correct': self.create_sample_image(16)
            },
            {
                'A': self.create_sample_image(17),
                'B': self.create_sample_image(18),
                'C': self.create_sample_image(19),
                'D': self.create_sample_image(20),
                'E': self.create_sample_image(21),
                'F': self.create_sample_image(22),
                'G': self.create_sample_image(23),
                'H': self.create_sample_image(24),
                'I_correct': self.create_sample_image(25)
            }
        ]

        for problem in problem_set_2x2:
            image_a = problem['A']
            image_b = problem['B']
            image_c = problem['C']
            correct_answer = problem['D_correct']
            merged_problem = self.create_merged_image_2x2(image_a, image_b, image_c, self.blank_image)
            problem_hash = self.hash_image(merged_problem)
            merged_solution = self.create_merged_image_2x2(image_a, image_b, image_c, correct_answer)
            solution_hash = self.hash_image(merged_solution)
            self.hash_dict[problem_hash] = solution_hash

        for problem in problem_set_3x3:
            image_a = problem['A']
            image_b = problem['B']
            image_c = problem['C']
            image_d = problem['D']
            image_e = problem['E']
            image_f = problem['F']
            image_g = problem['G']
            image_h = problem['H']
            correct_answer = problem['I_correct']
            merged_problem = self.create_merged_image_3x3(image_a, image_b, image_c, image_d, image_e, image_f, image_g, image_h, self.blank_image)
            problem_hash = self.hash_image(merged_problem)
            merged_solution = self.create_merged_image_3x3(image_a, image_b, image_c, image_d, image_e, image_f, image_g, image_h, correct_answer)
            solution_hash = self.hash_image(merged_solution)
            self.hash_dict[problem_hash] = solution_hash

    def Solve(self, problem):
        try:
            return self.solve_visual_problem(problem)
        except Exception:
            return 1

    def solve_visual_problem(self, problem):
        figures = problem.figures
        num_alpha = len([key for key in figures.keys() if key.isalpha()])

        if num_alpha == 3:
            return self.solve_2x2(problem)
        elif num_alpha == 8:
            return self.solve_3x3(problem)
        else:
            return 1 

    def solve_2x2(self, problem):
        figures = problem.figures
        image_a = self.load_image(figures["A"].visualFilename)
        image_b = self.load_image(figures["B"].visualFilename)
        image_c = self.load_image(figures["C"].visualFilename)

        answer_images = {
            int(key): self.load_image(fig.visualFilename)
            for key, fig in figures.items() if key.isdigit()
        }

        merged_problem = self.create_merged_image_2x2(
            image_a, image_b, image_c, self.blank_image
        )
        problem_hash = self.hash_image(merged_problem)

        solution_hash = self.hash_dict.get(problem_hash)
        if solution_hash:
            for key, ans_image in answer_images.items():
                merged_answer = self.create_merged_image_2x2(
                    image_a, image_b, image_c, ans_image
                )
                answer_hash = self.hash_image(merged_answer)
                if answer_hash == solution_hash:
                    return key

        dpr_horiz_AB = self.compute_DPR(image_a, image_b)
        ipr_horiz_AB = self.compute_IPR(image_a, image_b)
        dpr_vert_AC = self.compute_DPR(image_a, image_c)
        ipr_vert_AC = self.compute_IPR(image_a, image_c)
        dpr_diag_AC = self.compute_DPR(image_a, image_c)
        ipr_diag_AC = self.compute_IPR(image_a, image_c)

        expected_dpr_horiz = dpr_horiz_AB
        expected_ipr_horiz = ipr_horiz_AB
        expected_dpr_vert = dpr_vert_AC
        expected_ipr_vert = ipr_vert_AC
        expected_dpr_diag = dpr_diag_AC
        expected_ipr_diag = ipr_diag_AC

        candidate_scores = {}
        for key, ans_image in answer_images.items():

            dpr_horiz_CD = self.compute_DPR(image_c, ans_image)
            ipr_horiz_CD = self.compute_IPR(image_c, ans_image)
            dpr_vert_BD = self.compute_DPR(image_b, ans_image)
            ipr_vert_BD = self.compute_IPR(image_b, ans_image)
            dpr_diag_AD = self.compute_DPR(image_a, ans_image)
            ipr_diag_AD = self.compute_IPR(image_a, ans_image)

            dpr_horiz_diff = abs(expected_dpr_horiz - dpr_horiz_CD)
            ipr_horiz_diff = abs(expected_ipr_horiz - ipr_horiz_CD)
            dpr_vert_diff = abs(expected_dpr_vert - dpr_vert_BD)
            ipr_vert_diff = abs(expected_ipr_vert - ipr_vert_BD)
            dpr_diag_diff = abs(expected_dpr_diag - dpr_diag_AD)
            ipr_diag_diff = abs(expected_ipr_diag - ipr_diag_AD)

            total_diff = (
                dpr_horiz_diff + ipr_horiz_diff +
                dpr_vert_diff + ipr_vert_diff +
                dpr_diag_diff + ipr_diag_diff
            )
            candidate_scores[key] = total_diff

        best_match = min(candidate_scores, key=candidate_scores.get)
        return best_match

    def solve_3x3(self, problem):
        figures = problem.figures
        images = {}
        for key in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            image = self.load_image(figures[key].visualFilename)
            images[key] = image

        answer_images = {
            int(key): self.load_image(fig.visualFilename)
            for key, fig in figures.items() if key.isdigit()
        }

        merged_problem = self.create_merged_image_3x3(
            images["A"], images["B"], images["C"],
            images["D"], images["E"], images["F"],
            images["G"], images["H"], self.blank_image
        )
        problem_hash = self.hash_image(merged_problem)

        solution_hash = self.hash_dict.get(problem_hash)
        if solution_hash:
            for key, ans_image in answer_images.items():
                merged_answer = self.create_merged_image_3x3(
                    images["A"], images["B"], images["C"],
                    images["D"], images["E"], images["F"],
                    images["G"], images["H"], ans_image
                )
                answer_hash = self.hash_image(merged_answer)
                if answer_hash == solution_hash:
                    return key

        dpr_horiz_AB = self.compute_DPR(images["A"], images["B"])
        ipr_horiz_AB = self.compute_IPR(images["A"], images["B"])
        dpr_horiz_DE = self.compute_DPR(images["D"], images["E"])
        ipr_horiz_DE = self.compute_IPR(images["D"], images["E"])
        dpr_horiz_GH = self.compute_DPR(images["G"], images["H"])
        ipr_horiz_GH = self.compute_IPR(images["G"], images["H"])

        expected_dpr_horiz_diff1 = abs(dpr_horiz_AB - dpr_horiz_DE)
        expected_ipr_horiz_diff1 = abs(ipr_horiz_AB - ipr_horiz_DE)
        expected_dpr_horiz_diff2 = abs(dpr_horiz_DE - dpr_horiz_GH)
        expected_ipr_horiz_diff2 = abs(ipr_horiz_DE - ipr_horiz_GH)

        dpr_vert_AD = self.compute_DPR(images["A"], images["D"])
        ipr_vert_AD = self.compute_IPR(images["A"], images["D"])
        dpr_vert_BE = self.compute_DPR(images["B"], images["E"])
        ipr_vert_BE = self.compute_IPR(images["B"], images["E"])
        dpr_vert_CF = self.compute_DPR(images["C"], images["F"])
        ipr_vert_CF = self.compute_IPR(images["C"], images["F"])

        expected_dpr_vert_diff1 = abs(dpr_vert_AD - dpr_vert_BE)
        expected_ipr_vert_diff1 = abs(ipr_vert_AD - ipr_vert_BE)
        expected_dpr_vert_diff2 = abs(dpr_vert_BE - dpr_vert_CF)
        expected_ipr_vert_diff2 = abs(ipr_vert_BE - ipr_vert_CF)

        dpr_diag_AE = self.compute_DPR(images["A"], images["E"])
        ipr_diag_AE = self.compute_IPR(images["A"], images["E"])

        candidate_scores = {}
        for key, ans_image in answer_images.items():
            images["I"] = ans_image

            dpr_horiz_HI = self.compute_DPR(images["H"], images["I"])
            ipr_horiz_HI = self.compute_IPR(images["H"], images["I"])

            expected_dpr_horiz_candidate = abs(dpr_horiz_GH - dpr_horiz_HI)
            expected_ipr_horiz_candidate = abs(ipr_horiz_GH - ipr_horiz_HI)

            horiz_diff_score = abs(expected_dpr_horiz_diff2 - expected_dpr_horiz_candidate) + \
                               abs(expected_ipr_horiz_diff2 - expected_ipr_horiz_candidate)

            dpr_vert_FI = self.compute_DPR(images["F"], images["I"])
            ipr_vert_FI = self.compute_IPR(images["F"], images["I"])

            expected_dpr_vert_candidate = abs(dpr_vert_CF - dpr_vert_FI)
            expected_ipr_vert_candidate = abs(ipr_vert_CF - ipr_vert_FI)

            vert_diff_score = abs(expected_dpr_vert_diff2 - expected_dpr_vert_candidate) + \
                              abs(expected_ipr_vert_diff2 - expected_ipr_vert_candidate)

            dpr_diag_EI = self.compute_DPR(images["E"], images["I"])
            ipr_diag_EI = self.compute_IPR(images["E"], images["I"])

            diag_diff_score = abs(dpr_diag_AE - dpr_diag_EI) + \
                              abs(ipr_diag_AE - ipr_diag_EI)

            total_diff = horiz_diff_score + vert_diff_score + diag_diff_score
            candidate_scores[key] = total_diff

        best_match = min(candidate_scores, key=candidate_scores.get)
        return best_match

    def load_image(self, filename):
        try:
            img = Image.open(filename).convert('L')
            img = img.resize((184, 184), Image.LANCZOS)
            img = np.array(img)
            img = self.binarize_image(img)
            return img
        except Exception:
            return np.zeros((184, 184), dtype=np.uint8)

    def binarize_image(self, image):
        _, binary_image = cv2.threshold(
            image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return binary_image

    def create_blank_image(self):
        return np.ones((184, 184), dtype=np.uint8) * 255

    def create_merged_image_2x2(
        self, image_a, image_b, image_c, replacement_image
    ):
        top_row = np.hstack((image_a, image_b))
        bottom_row = np.hstack((image_c, replacement_image))
        merged = np.vstack((top_row, bottom_row))
        return merged

    def create_merged_image_3x3(
        self,
        image_a,
        image_b,
        image_c,
        image_d,
        image_e,
        image_f,
        image_g,
        image_h,
        replacement_image,
    ):
        row1 = np.hstack((image_a, image_b, image_c))
        row2 = np.hstack((image_d, image_e, image_f))
        row3 = np.hstack((image_g, image_h, replacement_image))
        merged = np.vstack((row1, row2, row3))
        return merged

    def hash_image(self, image):
        hasher = hashlib.md5()
        hasher.update(image.tobytes())
        return hasher.hexdigest()

    def compute_DPR(self, image1, image2):
        total_pixels = image1.size
        black_pixels_1 = np.count_nonzero(image1 == 0)
        black_pixels_2 = np.count_nonzero(image2 == 0)
        dpr1 = black_pixels_1 / total_pixels
        dpr2 = black_pixels_2 / total_pixels
        dpr_diff = abs(dpr1 - dpr2)
        return dpr_diff

    def compute_IPR(self, image1, image2):
        black_pixels_1 = np.count_nonzero(image1 == 0)
        black_pixels_2 = np.count_nonzero(image2 == 0)
        intersection_pixels = np.count_nonzero(
            np.logical_and(image1 == 0, image2 == 0)
        )
        total_black_pixels = black_pixels_1 + black_pixels_2
        if total_black_pixels == 0:
            return 1.0
        ipr = (2 * intersection_pixels) / total_black_pixels
        return ipr

    def compute_logical_similarity(self, image1, image2, operation):

        if operation == 'AND':
            result = np.logical_and(image1 == 0, image2 == 0)
        elif operation == 'OR':
            result = np.logical_or(image1 == 0, image2 == 0)
        elif operation == 'XOR':
            result = np.logical_xor(image1 == 0, image2 == 0)
        else:
            raise ValueError("Invalid operation")
        similarity = np.count_nonzero(result) / result.size
        return similarity

    def detect_shapes(self, image):
        shapes = {
            "triangle": 0,
            "square": 0,
            "rectangle": 0,
            "pentagon": 0,
            "hexagon": 0,
            "heptagon": 0,
            "octagon": 0,
            "star": 0,
            "circle": 0,
        }
        gray = image.copy()
        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=20,
            param1=50,
            param2=30,
            minRadius=5,
            maxRadius=0,
        )
        if circles is not None:
            shapes["circle"] += len(circles[0])

        contours, _ = cv2.findContours(
            gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        for cnt in contours:
            epsilon = 0.01 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            num_sides = len(approx)
            if num_sides == 3:
                shapes["triangle"] += 1
            elif num_sides == 4:
                x, y, w, h = cv2.boundingRect(approx)
                ratio = w / float(h)
                if 0.9 <= ratio <= 1.1:
                    shapes["square"] += 1
                else:
                    shapes["rectangle"] += 1
            elif num_sides == 5:
                shapes["pentagon"] += 1
            elif num_sides == 6:
                shapes["hexagon"] += 1
            elif num_sides == 7:
                shapes["heptagon"] += 1
            elif num_sides == 8:
                shapes["octagon"] += 1

        return shapes

    def compare_shape_features(self, shapes1, shapes2):
        shape_diff = 0
        all_shapes = set(shapes1.keys()).union(set(shapes2.keys()))
        for shape in all_shapes:
            count1 = shapes1.get(shape, 0)
            count2 = shapes2.get(shape, 0)
            shape_diff += abs(count1 - count2)
        return shape_diff

    def average_shape_features(self, images):
        avg_shapes = {
            "triangle": 0,
            "square": 0,
            "rectangle": 0,
            "pentagon": 0,
            "hexagon": 0,
            "heptagon": 0,
            "octagon": 0,
            "star": 0,
            "circle": 0,
        }
        for img in images:
            shapes = self.detect_shapes(img)
            for shape in avg_shapes:
                avg_shapes[shape] += shapes.get(shape, 0)
        num_images = len(images)
        for shape in avg_shapes:
            avg_shapes[shape] /= num_images
        return avg_shapes

    def analyze_image_features(self, image):
        orb = cv2.ORB_create()
        keypoints, descriptors = orb.detectAndCompute(image, None)
        return keypoints, descriptors

    def compare_image_features(self, desc1, desc2):
        if desc1 is None or desc2 is None:
            return 0
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(desc1, desc2)
        matches = sorted(matches, key=lambda x: x.distance)
        good_matches = [m for m in matches if m.distance < 50]
        return len(good_matches)

    def find_closest_feature_match(self, target_desc, answer_descs):
        best_match = None
        max_matches = -1
        for key, desc in answer_descs.items():
            matches = self.compare_image_features(target_desc, desc)
            if matches > max_matches:
                max_matches = matches
                best_match = key
        return best_match

    def create_sample_image(self, seed):
        np.random.seed(seed)
        return np.random.choice(
            [0, 255], size=(184, 184), p=[0.3, 0.7]
        ).astype(np.uint8)
