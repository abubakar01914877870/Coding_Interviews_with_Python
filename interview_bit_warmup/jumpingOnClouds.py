if __name__ == "__main__":

    c = [0, 0, 0, 1, 0, 0]


    def jumpingOnClouds(c):
        c.append('test')
        last_cloud = c[0]
        current_cloud = 0
        jump_count = 0
        double_jump = True
        for i in range(1, len(c) - 1):
            current_cloud = c[i]
            if last_cloud == 0 and current_cloud == 1:
                jump_count += 1
                last_cloud = current_cloud
                double_jump = True
            elif last_cloud == 0 and current_cloud == 0:
                jump_count += 1
                last_cloud = current_cloud
                if last_cloud == current_cloud == c[i + 1] and double_jump:
                    jump_count -= 1
                    double_jump = False
                else:
                    double_jump = True
            else:
                last_cloud = current_cloud
        return jump_count


    print(jumpingOnClouds(c))
